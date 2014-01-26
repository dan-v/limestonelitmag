# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Issue.published'
        db.add_column('magazine_issue', 'published', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Issue.published'
        db.delete_column('magazine_issue', 'published')


    models = {
        'magazine.article': {
            'Meta': {'object_name': 'Article'},
            'allow_preview': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['magazine.Author']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hits': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['magazine.Issue']"}),
            'subheading': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'magazine.author': {
            'Meta': {'ordering': "('surname', 'forename')", 'object_name': 'Author'},
            'details': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'magazine.issue': {
            'Meta': {'object_name': 'Issue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_date': ('django.db.models.fields.DateField', [], {}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['magazine']
