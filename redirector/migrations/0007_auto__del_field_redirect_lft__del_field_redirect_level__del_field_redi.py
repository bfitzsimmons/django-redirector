# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Redirect.lft'
        db.delete_column('redirector_redirect', 'lft')

        # Deleting field 'Redirect.level'
        db.delete_column('redirector_redirect', 'level')

        # Deleting field 'Redirect.tree_id'
        db.delete_column('redirector_redirect', 'tree_id')

        # Deleting field 'Redirect.rght'
        db.delete_column('redirector_redirect', 'rght')


        # Changing field 'Redirect.parent'
        db.alter_column('redirector_redirect', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['redirector.Redirect']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Redirect.lft'
        raise RuntimeError("Cannot reverse this migration. 'Redirect.lft' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Redirect.level'
        raise RuntimeError("Cannot reverse this migration. 'Redirect.level' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Redirect.tree_id'
        raise RuntimeError("Cannot reverse this migration. 'Redirect.tree_id' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Redirect.rght'
        raise RuntimeError("Cannot reverse this migration. 'Redirect.rght' and its values cannot be restored.")

        # Changing field 'Redirect.parent'
        db.alter_column('redirector_redirect', 'parent_id', self.gf('mptt.fields.TreeForeignKey')(null=True, to=orm['redirector.Redirect']))

    models = {
        'redirector.redirect': {
            'Meta': {'unique_together': "(('site', 'url'),)", 'object_name': 'Redirect'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['redirector.Redirect']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'redirect_site'", 'to': "orm['sites.Site']"}),
            'url': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['redirector']