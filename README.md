## Information Retrieval Project For 5th year ITE .

### The prurpose of this project is to make simple information retrieval system

#### pre requests to run this project

- Django

  ## first check if you have already Django installed in your machine by entering this command in terminal

  ```
  python -m django --version
  ```

  . if you dont have it then install it then continue

  - #### run project

  ```
    python manage.py runserver
  ```

## PS: our api starts from /api/v1

### project architecture

#### we create 3 classes for this project as follow

- DataSetOperations : contains functionality that deals with provided datasets (cacm and cisi) such as
  - preprocess_docs : which take file and preprocess it ( remove indicators such as .I , .A,.W,.B in supervised way) then save the result into python dict
  - preprocess_rel : same as preprocess_docs but for relations file only , because it appear that we can handle it using pandas instead of default way in handling files
- DataProcessing : contains functionality about nlp such as
  - tokenize words
  - normalization
  - lemmatization
  - stemming
  - correct words
  - and finally save results to file after preprocessing
- IROperations: contains
  - transform_to_tfidf : to get tfidf for set of documents
  - word_embedding : getting vector for each document in set of documents
  - get_similarity : get cosine similarity between query and set of documents
  - precision : caclulate precision of retrieved documents

### in Django views

we use all 3 classes together in oreder to

- get the two datasets , preprocess them then save each one to a file , just in first time
- use the saved data from previous step to get documents relative to a query

# for more details about how we make this project please check the attached pdf
