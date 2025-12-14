## System Architecture

AI Systems Lab follows a modular, layered architecture. I adopted this from different tutorials I checked on Kaggle

### High-Level Components

1. Data Layer
   - Raw data ingestion
   - Validation and preprocessing
   - Feature generation

2. ML Layer
   - Training pipelines
   - Evaluation logic
   - Model artifacts

3. NLP Layer
   - Embeddings generation
   - Semantic indexing
   - Retrieval logic

4. Service Layer
   - Business logic
   - Orchestration
   - Analytics

5. API Layer
   - FastAPI endpoints
   - Input/output schemas
   - Authentication (future)


### Design Principles

- Separation of concerns
- Explicit data flow
- Reproducibility
- Testability
- Deployment-first mindset
