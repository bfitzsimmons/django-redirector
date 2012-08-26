# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Redirect'
        db.create_table('redirector_redirect', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='redirect_site', to=orm['sites.Site'])),
            ('from_url', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('to_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True, null=True, blank=True)),
        ))
        db.send_create_signal('redirector', ['Redirect'])

        # Adding unique constraint on 'Redirect', fields ['site', 'from_url']
        db.create_unique('redirector_redirect', ['site_id', 'from_url'])


    def backwards(self, orm):
        # Removing unique constraint on 'Redirect', fields ['site', 'from_url']
        db.delete_unique('redirector_redirect', ['site_id', 'from_url'])

        # Deleting model 'Redirect'
        db.delete_table('redirector_redirect')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'redirector.redirect': {
            'Meta': {'unique_together': "(('site', 'from_url'),)", 'object_name': 'Redirect'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'from_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'redirect_site'", 'to': "orm['sites.Site']"}),
            'to_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['redirector']