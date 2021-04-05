# from atributes_and_methods.exe.document_management.project_14134.category import Category
# from atributes_and_methods.exe.document_management.project_14134.document import Document
# from atributes_and_methods.exe.document_management.project_14134.topic import Topic

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        result = '\n'.join([repr(d) for d in self.documents])
        return result

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        cat_to_edit = [c for c in self.categories if c._id == category_id][0]
        cat_to_edit.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_to_edit = [t for t in self.topics if t._id == topic_id][0]
        topic_to_edit.topic = new_topic
        topic_to_edit.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc_to_edit = [d for d in self.documents if d._id == document_id][0]
        doc_to_edit.file_name = new_file_name

    def delete_category(self, category_id):
        cat_to_del = [c for c in self.categories if c._id == category_id][0]
        self.categories.remove(cat_to_del)

    def delete_topic(self, topic_id):
        topic_to_del = [t for t in self.topics if t._id == topic_id][0]
        self.topics.remove(topic_to_del)

    def delete_document(self, document_id):
        doc_to_del = [d for d in self.documents if d._id == document_id][0]
        self.documents.remove(doc_to_del)

    def get_document(self, document_id):
        doc_to_get = [d for d in self.documents if d._id == document_id][0]
        return doc_to_get


# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project_14134")
# d2 = Document(2, 2, 2, "second project_14134")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
# storage.add_document(d2)
# storage.edit_topic(1, "new", "new storage")
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
