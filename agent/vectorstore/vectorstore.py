import uuid
from typing import Any

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document
from langchain_openai.embeddings import OpenAIEmbeddings

class VectorStore:
    #TODO: Implement the vector store for the agent.
    # This class will be used to store the vectors of the documents.

    def __init__(self, agent):
        self.vector_store = InMemoryVectorStore(self.get_embedding)
        self._initialize_vector_store()
        

    @property
    def get_embedding(self):
        return OpenAIEmbeddings()
    

    def _initialize_vector_store(self):
        knowledges = self._get_all_base_knowledge()
        self.vector_store.add_documents(knowledges)


    def _get_all_base_knowledge(self) -> list[Document]:
        from ..utils.knowledge import Intents
        intents = Intents.get_all_intents()
        
        knowledges = []
        for intent in intents:
            knowledge = Document(
                page_content=intent[1], 
                metadata={
                    "id": intent[0],
                    "domain": "intents"
                }
            )
            knowledges.append(knowledge)

        return knowledges



    def wrap_chunk(
        self,
        text: str,
        metadata: dict
    ) -> Document:
        
        return Document(
            page_content=text, 
            metadata=metadata
        )
    

    async def add_knowledge(
        self,
        documents: list[Document],
        ids: list[str] | None = None
    ) -> Any:
        
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in documents]

        await self.vector_store.aadd_documents(
            documents=documents,
            ids=ids
        )


    async def do_similarity_search(
        self,
        query: str,
        k: int = 3,
        filter: dict | None = None,
        **kwargs: dict
    ) -> list[Document]:
        
        knowledges = await self.vector_store.asimilarity_search(
            query=query,
            k=k,
            **kwargs
        )

        for k, v in filter.items():
            if filter:
                knowledges = [
                    knowledge for knowledge in knowledges 
                    if knowledge.metadata.get(k) == v
                ]

        return knowledges
    

if __name__ == "__main__":
    VectorStore()