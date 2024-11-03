---

# RIOT-AGENT

🤖 리그 오브 레전드용 에이전트

---

## 한국어

### 📜 프로젝트 설명
`RIOT-AGENT`는 인기 온라인 게임 리그 오브 레전드에서 데이터를 수집하고 분석하기 위해 설계된 자동화된 에이전트입니다. 플레이어 통계, 매치 기록, 챔피언 정보를 제공하여 데이터 기반의 의사결정과 인사이트를 지원하는 것이 목표입니다.

### 🦜 주요 기능
- 플레이어(소환사) 정보 조회
- 챔피언 통계 및 능력 조회
- 최근 매치 기록 및 상세 정보 가져오기
- 랭크 성과와 리더보드 순위 분석
- 전략 강화를 위한 게임 내 아이템 정보 수집

### ⚙️ 작동 방식

![파이프라인 다이어그램](./docs/images/pipeline.png)

1. 쿼리의 의도를 파악합니다.
2. 의도에 따라 메인 작업을 계획합니다.
3. 메인 작업을 비동기로 수행합니다.
4. 모든 메인 작업이 완료되면 **동적 계획(dynamical planning)**을 통해 서브 작업을 계획합니다.
5. 서브 작업을 비동기로 수행합니다.
6. 모든 작업에서 수집한 데이터를 취합하여 최종 답변을 위한 전처리를 수행합니다.
7. 최종 답변을 에이전트로부터 받습니다.

### 📝 동적 계획 (Dynamical Planning)

동적 계획이란 에이전트가 작업 풀에서 함수를 동적으로 선택하는 것을 의미합니다.
이 기능을 구현하기 위해 몇 가지 조건이 필요합니다.

- 각 작업 함수는 **반환값이 없어야 하며(VOID 반환)** **고정된 입력 매개변수**를 가져야 합니다.

LLM 기반 에이전트는 입력 매개변수와 반환값을 정확히 결정할 수 없으므로, 에이전트가 함수만 선택하도록 해야 합니다.

- 각 작업 함수는 **문서화된 문자열(docstring)을 반드시 포함**해야 합니다.

문서화 문자열은 함수가 어떤 작업을 수행하는지 LLM에게 가장 잘 전달할 수 있는 방법입니다.
예제에서 에이전트는 먼저 LLM을 시도하고, 예외가 발생할 경우 문서화 문자열을 통해 유사도를 검색합니다.

### 💼 메인 작업과 서브 작업의 차이점

**그렇다면 차이점은 무엇일까요?**

사용자의 쿼리에서 의도를 파악할 수 있으며, 각 의도에 1부터 6까지 번호를 지정합니다.
의도를 이해하는 이유는 서브 작업을 수행하기 위해 필요한 사전 확인 작업을 파악하기 위함입니다.

예를 들어, 모든 챔피언 정보를 `QueryWrapper`에 가져오는 것은 서브 작업에 필요하지 않은 일입니다.
이 작업은 서브 작업을 준비하기 위해 미리 수행되어야 합니다.

또한, 서브 작업은 매개변수 조정 및 세부적인 행동 조절이 제한적입니다.
따라서 의도 기반의 메인 작업을 수행하여 이러한 세부 작업을 조정하고 서브 작업에 필요한 정보를 미리 가져오도록 합니다.