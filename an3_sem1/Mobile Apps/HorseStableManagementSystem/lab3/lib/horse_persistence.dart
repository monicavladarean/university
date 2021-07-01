import 'dart:async';

import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';
import 'package:flutter/widgets.dart';
import 'horse.dart';

class HorsePersistence
{
  Future<Database> database;

  HorsePersistence()
  {
    WidgetsFlutterBinding.ensureInitialized();
    database = _connect();
  }

  Future<Database> _connect() async
  {
    return openDatabase(
      join(await getDatabasesPath(), 'HorsesDB.db'),
      onCreate: (db, version) {
        return db.execute(
          "CREATE TABLE horses(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, breed TEXT, food TEXT, disease TEXT)",
        );
      },
      version: 1,
    );
  }

  Future<void> insertHorse(Horse horse) async
  {
    final Database db = await database;

    await db.insert(
      'horses',
      horse.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
  }

  Future<List<Horse>> horses() async
  {
    final Database db = await database;
    final List<Map<String, dynamic>> maps = await db.query('horses');

    return List.generate(maps.length, (i)
    {
      return Horse(
        id: maps[i]['id'],
        name: maps[i]['name'],
        age: maps[i]['age'],
        breed: maps[i]['breed'],
        food: maps[i]['food'],
        disease: maps[i]['disease'],
      );
    });
  }

  Future<void> updateHorse(Horse horse) async
  {
    final db = await database;

    await db.update(
      'horses',
      horse.toMap(),
      where: "id = ?",
      whereArgs: [horse.id],
    );
  }

  Future<void> deleteHorse(int id) async
  {
    final db = await database;

    await db.delete
      (
      'horses',
      where: "id = ?",
      whereArgs: [id],
    );
  }

  Future<void> deleteAllData() async
  {
    final db = await database;

    await db.delete('horses');
  }
}
