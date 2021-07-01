import 'dart:collection';

import 'package:flutter/cupertino.dart';
import 'package:lab3/horse.dart';
import 'package:lab3/horse_persistence.dart';
import 'package:connectivity/connectivity.dart';
import 'package:lab3/horse_api_provider.dart';
import 'dart:developer';

class HorseNotifier with ChangeNotifier
{
  HorseApiProvider _horseApiProvider;
  HorsePersistence _horsePersistence;
  List<Horse> _horses;

  HorseNotifier()
  {
    _horseApiProvider = HorseApiProvider();
    _horsePersistence = HorsePersistence();
    _horses = List<Horse>();
    _syncData();
  }

  void _syncData() async
  {
    await _loadDataToMemory();
    try
    {
      var connected = await (Connectivity().checkConnectivity());

      if (connected == ConnectivityResult.mobile || connected == ConnectivityResult.wifi)
      {
        //_horseApiProvider.syncData(_horses);
      }
    }
    catch (e)
    {
      log('Data sync failed');
    }
  }

  void _loadDataToMemory() async
  {
    _horses = await _horsePersistence.horses();
    notifyListeners();
  }

  UnmodifiableListView<Horse> get horses => UnmodifiableListView(_horses);

  Horse horse(int id)
  {
    return _horses.firstWhere((element) => element.id == id,
        orElse: () => Horse(
            id: -1,
            name: 'Not found',
            age: 0,
            breed: 'Not found',
            food: 'not found',
            disease: 'not found'));
  }

  void add(String name, int age, String breed, String food, String disease)
  {
    final horse = Horse(
        id: null,
        name: name,
        age: age,
        breed: breed,
        food: food,
        disease: disease);

    _postHorse(horse);
    _horsePersistence.insertHorse(horse);
    _loadDataToMemory();
  }

  void _postHorse(horse) async
  {
    var connected = await (Connectivity().checkConnectivity());
    if (connected == ConnectivityResult.mobile || connected == ConnectivityResult.wifi)
    {
      _horseApiProvider.postHorse(horse);
    }
  }

  void update(int id, String name, int age, String breed, String food, String disease)
  {
    final horse = Horse(
        id: id,
        name: name,
        age: age,
        breed: breed,
        food: food,
        disease: disease);
    _putHorse(horse);
    _horsePersistence.updateHorse(horse);
    _loadDataToMemory();
  }

  void _putHorse(horse) async
  {
    var connected = await (Connectivity().checkConnectivity());
    if (connected == ConnectivityResult.mobile || connected == ConnectivityResult.wifi)
    {
      _horseApiProvider.putHorse(horse);
    }
  }

  void remove(int id)
  {
    _deleteHorse(id);
    _horsePersistence.deleteHorse(id);
    _loadDataToMemory();
  }

  void _deleteHorse(id) async
  {
    var connected = await (Connectivity().checkConnectivity());
    if (connected == ConnectivityResult.mobile || connected == ConnectivityResult.wifi)
    {
      _horseApiProvider.deleteHorse(id);
    }
  }
}