# -*- coding: utf-8 -*-
import datetime
import re
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        regex = r"(.*?)\((.*)\)"
        r = re.compile(regex)

        Player = orm.Player
        q = Player.objects.filter(name__iregex=regex)
        for p in q:
            n = p.name
            m = r.match(n)
            p.romanized_name = m.group(1).strip()
            p.name = m.group(2).strip()
            print(("{} -> N: {} R: {}").format(n, p.name, p.romanized_name))
            p.save()

    def backwards(self, orm):
        Player = orm.Player
        q = Player.objects.filter(name__isnull=False, romanized_name__isnull=False)
        for p in q:
            p.name = "{} ({})".format(p.romanized_name, p.name)
            p.romanized_name = None
            p.save()

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ratings.alias': {
            'Meta': {'object_name': 'Alias', 'db_table': "'alias'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Group']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']", 'null': 'True'})
        },
        'ratings.apikey': {
            'Meta': {'object_name': 'APIKey', 'db_table': "'apikey'"},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_opened': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True', 'primary_key': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'requests': ('django.db.models.fields.IntegerField', [], {})
        },
        'ratings.balanceentry': {
            'Meta': {'object_name': 'BalanceEntry', 'db_table': "'balanceentry'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_gains': ('django.db.models.fields.FloatField', [], {}),
            'pvt_losses': ('django.db.models.fields.IntegerField', [], {}),
            'pvt_wins': ('django.db.models.fields.IntegerField', [], {}),
            'pvz_losses': ('django.db.models.fields.IntegerField', [], {}),
            'pvz_wins': ('django.db.models.fields.IntegerField', [], {}),
            't_gains': ('django.db.models.fields.FloatField', [], {}),
            'tvz_losses': ('django.db.models.fields.IntegerField', [], {}),
            'tvz_wins': ('django.db.models.fields.IntegerField', [], {}),
            'z_gains': ('django.db.models.fields.FloatField', [], {})
        },
        'ratings.earnings': {
            'Meta': {'object_name': 'Earnings', 'db_table': "'earnings'", 'ordering': "['-earnings']"},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'earnings': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origearnings': ('django.db.models.fields.DecimalField', [], {'decimal_places': '8', 'max_digits': '20'}),
            'placement': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"})
        },
        'ratings.event': {
            'Meta': {'object_name': 'Event', 'db_table': "'event'", 'ordering': "['idx', 'latest', 'fullname']"},
            'big': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'earliest': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'family': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ratings.Event']", 'through': "orm['ratings.EventAdjacency']"}),
            'fullname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500'}),
            'homepage': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idx': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'latest': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'lft': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'noprint': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_event'", 'to': "orm['ratings.Event']", 'blank': 'True', 'null': 'True'}),
            'prizepool': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'rgt': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'tl_thread': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tlpd_db': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tlpd_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'})
        },
        'ratings.eventadjacency': {
            'Meta': {'object_name': 'EventAdjacency', 'db_table': "'eventadjacency'"},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'uplink'", 'to': "orm['ratings.Event']"}),
            'distance': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'downlink'", 'to': "orm['ratings.Event']"})
        },
        'ratings.group': {
            'Meta': {'object_name': 'Group', 'db_table': "'group'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'disbanded': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'founded': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'homepage': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'meanrating': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ratings.Player']", 'through': "orm['ratings.GroupMembership']"}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'}),
            'scoreak': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'scorepl': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '25'})
        },
        'ratings.groupmembership': {
            'Meta': {'object_name': 'GroupMembership', 'db_table': "'groupmembership'"},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'playing': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'})
        },
        'ratings.match': {
            'Meta': {'object_name': 'Match', 'db_table': "'match'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'eventobj': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Event']", 'blank': 'True', 'null': 'True'}),
            'game': ('django.db.models.fields.CharField', [], {'default': "'WoL'", 'db_index': 'True', 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Period']"}),
            'pla': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_pla'", 'to': "orm['ratings.Player']"}),
            'plb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_plb'", 'to': "orm['ratings.Player']"}),
            'rca': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1'}),
            'rcb': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1'}),
            'rta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rta'", 'to': "orm['ratings.Rating']", 'null': 'True'}),
            'rtb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rtb'", 'to': "orm['ratings.Rating']", 'null': 'True'}),
            'sca': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'scb': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'blank': 'True', 'null': 'True'}),
            'treated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ratings.message': {
            'Meta': {'object_name': 'Message', 'db_table': "'message'"},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Event']", 'null': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Group']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Match']", 'null': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'params': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']", 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'ratings.period': {
            'Meta': {'object_name': 'Period', 'db_table': "'period'"},
            'computed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'dom_p': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dom_t': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dom_z': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_recompute': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'num_games': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_newplayers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_retplayers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start': ('django.db.models.fields.DateField', [], {'db_index': 'True'})
        },
        'ratings.player': {
            'Meta': {'object_name': 'Player', 'db_table': "'player'", 'ordering': "['tag']"},
            'birthday': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '2', 'null': 'True', 'db_index': 'True'}),
            'current_rating': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'current'", 'to': "orm['ratings.Rating']", 'blank': 'True', 'null': 'True'}),
            'dom_end': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_dom_end'", 'to': "orm['ratings.Period']", 'blank': 'True', 'null': 'True'}),
            'dom_start': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_dom_start'", 'to': "orm['ratings.Period']", 'blank': 'True', 'null': 'True'}),
            'dom_val': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'mcnum': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '1'}),
            'romanized_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'sc2e_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '30'}),
            'tlpd_db': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'tlpd_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'ratings.prematch': {
            'Meta': {'object_name': 'PreMatch', 'db_table': "'prematch'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.PreMatchGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pla': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prematch_pla'", 'to': "orm['ratings.Player']", 'blank': 'True', 'null': 'True'}),
            'pla_string': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'plb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prematch_plb'", 'to': "orm['ratings.Player']", 'blank': 'True', 'null': 'True'}),
            'plb_string': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'rca': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1'}),
            'rcb': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1'}),
            'sca': ('django.db.models.fields.SmallIntegerField', [], {}),
            'scb': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'ratings.prematchgroup': {
            'Meta': {'object_name': 'PreMatchGroup', 'db_table': "'prematchgroup'"},
            'contact': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'max_length': '200'}),
            'game': ('django.db.models.fields.CharField', [], {'default': "'wol'", 'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True', 'null': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'default': "''", 'blank': 'True', 'null': 'True', 'max_length': '500'})
        },
        'ratings.rating': {
            'Meta': {'object_name': 'Rating', 'db_table': "'rating'", 'ordering': "['period']"},
            'bf_dev': ('django.db.models.fields.FloatField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
            'bf_dev_vp': ('django.db.models.fields.FloatField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
            'bf_dev_vt': ('django.db.models.fields.FloatField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
            'bf_dev_vz': ('django.db.models.fields.FloatField', [], {'default': '1', 'blank': 'True', 'null': 'True'}),
            'bf_rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vp': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vt': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vz': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'comp_rat': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'comp_rat_vp': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'comp_rat_vt': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'comp_rat_vz': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'decay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dev': ('django.db.models.fields.FloatField', [], {}),
            'dev_vp': ('django.db.models.fields.FloatField', [], {}),
            'dev_vt': ('django.db.models.fields.FloatField', [], {}),
            'dev_vz': ('django.db.models.fields.FloatField', [], {}),
            'domination': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Period']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vp': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vt': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vz': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'prev': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prevrating'", 'to': "orm['ratings.Rating']", 'null': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'rating_vp': ('django.db.models.fields.FloatField', [], {}),
            'rating_vt': ('django.db.models.fields.FloatField', [], {}),
            'rating_vz': ('django.db.models.fields.FloatField', [], {})
        },
        'ratings.story': {
            'Meta': {'object_name': 'Story', 'db_table': "'story'", 'ordering': "['date']"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Event']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'params': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"})
        }
    }

    complete_apps = ['ratings']
    symmetrical = True
