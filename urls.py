from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',  views.homepage, name='homepage'),
    url(r'^pilot/$',  views.pilot, name='pilot'),
    url(r'^costs/$',  views.costs, name='costs'),
    url(r'^benefits/$',  views.benefits, name='benefits'),
    url(r'^target/$',  views.target, name='target'),
    url(r'^entry/$',  views.entry, name='entry'),
    url(r'^television/$',  views.television, name='television'),
    url(r'^pdf/$',  views.pdf, name='pdf'),
    url(r'^contact/$',  views.contact, name='contact'),
    url(r'^preproduction/$',  views.preproduction, name='preproduction'),
    url(r'^production/$',  views.production, name='production'),
    url(r'^postproduction/$',  views.postproduction, name='postproduction'),
    url(r'^whatisit/$',  views.whatisit, name='whatisit'),
    url(r'^howdoijoin/$',  views.howdoijoin, name='howdoijoin'),
    url(r'^whataretherules/$',  views.whataretherules, name='whataretherules'),
    url(r'^whocanjoin/$',  views.whocanjoin, name='whocanjoin'),
    url(r'^whowinswhat/$',  views.whowinswhat, name='whowinswhat'),
    url(r'^schedule/$',  views.schedule, name='schedule'),

]
