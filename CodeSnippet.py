#!/usr/bin/env python
# coding: utf-8

# In[1]:


class CodeSnippet:
    def __init__(self, title, code, language, tags):
        self.title = title
        self.code = code
        self.language = language
        self.tags = tags

class CodeSnippetManager:
    def __init__(self):
        self.snippets = []  # Store code snippets

    def add_snippet(self, title, code, language, tags):
        snippet = CodeSnippet(title, code, language, tags)
        self.snippets.append(snippet)
        print("Code snippet added successfully.")

    def search_by_language(self, language):
        matching_snippets = [snippet for snippet in self.snippets if snippet.language == language]
        if matching_snippets:
            print(f"Found {len(matching_snippets)} snippets for language '{language}':")
            for snippet in matching_snippets:
                print(f"Title: {snippet.title}, Tags: {', '.join(snippet.tags)}")
        else:
            print(f"No snippets found for language '{language}'.")

    def search_by_tag(self, tag):
        matching_snippets = [snippet for snippet in self.snippets if tag in snippet.tags]
        if matching_snippets:
            print(f"Found {len(matching_snippets)} snippets for tag '{tag}':")
            for snippet in matching_snippets:
                print(f"Title: {snippet.title}, Language: {snippet.language}")
        else:
            print(f"No snippets found for tag '{tag}'.")

# Example usage:
snippet_manager = CodeSnippetManager()

# Add code snippets
snippet_manager.add_snippet("Hello World in Python", "print('Hello, World!')", "Python", ["hello", "beginner"])
snippet_manager.add_snippet("Bubble Sort in Python", "def bubble_sort(arr): ...", "Python", ["sorting", "algorithm"])
snippet_manager.add_snippet("Quick Sort in C++", "void quickSort(int arr[], int low, int high) { ... }", "C++", ["sorting", "algorithm"])

# Search by language
snippet_manager.search_by_language("Python")

# Search by tag
snippet_manager.search_by_tag("algorithm")


# In[ ]:




