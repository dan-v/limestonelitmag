from django.conf.urls import patterns, url, include
from magazine.views import (CurrentIssueListView, IssueListView, IssueView,
                            ArticleView, AuthorListView,
                            AuthorListViewAlphabetised, AuthorDetailView,
                            BookReviewView, AuthorArticlesView,
                            AuthorBookReviewsView, submit, about)

urlpatterns = patterns(
    '',
    url(r'^$', CurrentIssueListView.as_view(), name='magazine_index'),
    url(r'^issues/$', IssueListView.as_view(), name='magazine_issues'),
    url(r'^issues/(?P<number>([0-9]+))/$', IssueView.as_view(),
        name='magazine_issue_detail'),
    url(r'^issues/(?P<number>([0-9]+))/(?P<pk>([0-9]+))/$',
        ArticleView.as_view(), name='magazine_article_detail'),
    url(r'^issues/(?P<number>([0-9]+))/reviews/(?P<pk>([0-9]+))/$',
        BookReviewView.as_view(), name='magazine_bookreview_detail'),
    url(r'^authors/$', AuthorListView.as_view(), name='magazine_authors'),
    url(r'^authors/alphabetised/$',
        AuthorListViewAlphabetised.as_view(),
        name='magazine_authors_alphabetised'),
    url(r'^authors/(?P<pk>([0-9]+))/$',
        AuthorDetailView.as_view(), name='magazine_author_detail'),
    url(r'^authors/(?P<pk>([0-9]+))/articles/$',
        AuthorArticlesView.as_view(), name='magazine_author_articles'),
    url(r'^authors/(?P<pk>([0-9]+))/reviews/$',
        AuthorBookReviewsView.as_view(), name='magazine_author_book_reviews'),
    url(r'^submit', submit, name='submit'),
    url(r'^about', about, name='about')    
)
