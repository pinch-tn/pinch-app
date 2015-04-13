# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.key'
        db.add_column(u'walkthrough_project', 'key',
                      self.gf('randomslugfield.fields.RandomSlugField')(exclude_lower=False, length=6, max_length=6, exclude_digits=False, blank=False, default=None, exclude_vowels=False, exclude_upper=True, null=True),
                      keep_default=False)


        # Changing field 'Project.slug'
        db.alter_column(u'walkthrough_project', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', populate_from=['name', 'key'], overwrite=False))

    def backwards(self, orm):
        # Deleting field 'Project.key'
        db.delete_column(u'walkthrough_project', 'key')


        # Changing field 'Project.slug'
        db.alter_column(u'walkthrough_project', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(populate_from='name', allow_duplicates=False, max_length=50, separator=u'-', overwrite=False))

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
            'ended': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'key': ('randomslugfield.fields.RandomSlugField', [], {'exclude_lower': 'False', 'length': '6', 'max_length': '6', 'exclude_digits': 'False', 'blank': 'True', 'exclude_vowels': 'False', 'exclude_upper': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "['name', 'key']", 'overwrite': 'False'}),
            'started': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'tools': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_customer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_offering': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'validate_value_prop': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
