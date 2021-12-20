#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module performs a unittest on storage.py"""

import random
import unittest

from storage import Repo
from storage import StorageError

from test_assets import create_random_templates


repo = Repo()
repo = create_random_templates(repo=repo)


class TestStorage(unittest.TestCase):
    """Perform unittest on storage.py."""

    def test_instantiate_templates(self):
        """Test Repo._instantiate_templates() to confirm objects are being instantiated correctly."""

        # Confirm that created objects are of the appropriate class.
        for objects, templates in repo.templates.items():
            for template in templates:
                self.assertIsInstance(template, repo.note_classes[objects])

    def test_id_duplicates(self):
        """Test Repo._id to confirm it is not storing duplicate values."""

        id_2 = set(repo.ids)  # Make a set version of repo._id to eliminate possible duplicates.
        self.assertEqual(len(repo.ids), len(id_2))

    def test_add_id(self):
        """Test Repo._add_id to confirm that it will not add duplicate id's. or store id's of the wrong length"""

        duplicate = random.choice(repo.ids)
        with self.assertRaises(StorageError):
            repo._add_id(duplicate)
        with self.assertRaises(StorageError):
            duplicate = str(duplicate)
            duplicate = duplicate + '1'  # Add one to the allowable digit length.
            repo._add_id(int(duplicate))


if __name__ == '__main__':
    unittest.main()
