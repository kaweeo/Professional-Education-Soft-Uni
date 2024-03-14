from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        searched_category = next(filter(lambda c: c.id == category_id, self.categories))
        searched_category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        searched_topic = next(filter(lambda t: t.id == topic_id, self.topics))
        searched_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        searched_doc = next(filter(lambda d: d.id == document_id, self.documents))
        searched_doc.edit(new_file_name)

    def delete_topic(self, topic_id: int) -> None:
        topic = next(filter(lambda t: t.id == topic_id, self.topics))
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = next(filter(lambda d: d.id == document_id, self.documents))
        self.documents.remove(document)

    def delete_category(self, category_id: int) -> None:
        category = next(filter(lambda c: c.id == category_id, self.categories))
        self.categories.remove(category)

    def __repr__(self):
        return "\n".join(str(doc) for doc in self.documents)
