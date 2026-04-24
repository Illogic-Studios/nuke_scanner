# Nuke Scanner

> A few tools that help simplify cleaning nuke scripts 
---
 
## Table of Contents
 
- [Prism folder structure](#prism-folder-structure)
- [Features](#features)
  - [Select unconnected nodes - `select_unconnected_read.py`](#select-unconnected-read)
  - [Scan nuke scene and tag renders to delete — `nuke_scanner.py`](#nuke-scanner)
  - [Delete tagged renders — `nuke_delete.py`](#nuke-delete)

---
 
## Prism folder structure
 
 The tool expects this layout:
 
```
I:/<PROJECT>/03_Production/Shots/<SEQUENCE>/<SHOT>/
├── Scenefiles/
│   └── Compo/
│       └── Compo/
│           └── ...
└── Renders/
    ├── 3dRender/
        └── ...
```
---

## Features

### Select unconnected read

This first tool simply selects all "READ" nodes that are not connected to any "WRITE" node.
This selection will allow the artist to decide the actions to do with the nodes that are selected (i.e. delete them to clear the scene). 

### Nuke scanner

Parses your nuke scene for all used versions of the renders, then parses the renders directory and tags all unused renders with "_TO_DELETE_" as prefix. 

This does not automatically delete any file or folder.

### Nuke delete 

Parses the render folder for every tool tagged with "_TO_DELETE_", and deletes them. 
It is usually best to use this after having run the ["Nuke scanner"](#nuke-scanner) in order to have all unnecessary versions tagged to delete. These two tools were seperated to avoid any unwanted deletions, and allow as much manual security as possible.