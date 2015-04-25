# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Project', fields ['name']
        db.delete_unique(u'walkthrough_project', ['name'])

        # Adding field 'Project.email_sent'
        db.add_column(u'walkthrough_project', 'email_sent',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding unique constraint on 'Project', fields ['slug']
        db.create_unique(u'walkthrough_project', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Project', fields ['slug']
        db.delete_unique(u'walkthrough_project', ['slug'])

        # Deleting field 'Project.email_sent'
        db.delete_column(u'walkthrough_project', 'email_sent')

        # Adding unique constraint on 'Project', fields ['name']
        db.create_unique(u'walkthrough_project', ['name'])


    models = {
        u'walkthrough.mvp': {
            'Meta': {'object_name': 'Mvp'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_statement': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['walkthrough.Project']", 'unique': 'True'})
        },
        u'walkthrough.mvpredaction': {
            'Meta': {'object_name': 'MvpRedaction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Mvp']"}),
            'statement_end': ('django.db.models.fields.IntegerField', [], {}),
            'statement_start': ('django.db.models.fields.IntegerField', [], {})
        },
        u'walkthrough.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ended': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'key': ('randomslugfield.fields.RandomSlugField', [], {'exclude_lower': 'False', 'exclude_digits': 'False', 'exclude_vowels': 'False', 'exclude_upper': 'True', 'length': '6', 'max_length': '6', 'blank': 'True', 'unique': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "['name', 'key']", 'overwrite': 'False'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tools': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_customer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_offering': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_value_prop': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'walkthrough.projectmember': {
            'Meta': {'object_name': 'ProjectMember'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'to': u"orm['walkthrough.Project']"})
        },
        u'walkthrough.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Mvp']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'workstream': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Workstream']"})
        },
        u'walkthrough.workstream': {
            'Meta': {'unique_together': "(('name', 'mvp'),)", 'object_name': 'Workstream'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'mvp': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['walkthrough.Mvp']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'statement_end': ('django.db.models.fields.IntegerField', [], {}),
            'statement_start': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['walkthrough']