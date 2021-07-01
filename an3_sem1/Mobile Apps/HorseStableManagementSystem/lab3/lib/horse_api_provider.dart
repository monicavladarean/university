import 'package:lab3/horse.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:developer';

class HorseApiProvider {
  static const HORSES_URL = 'http://10.0.2.2:8000/horses/';

  List<Horse> _parseHorses(String responseBody)
  {
    final parsed = jsonDecode(responseBody).cast<Map<String, dynamic>>();

    return parsed.map<Horse>((json) => Horse.fromJson(json)).toList();
  }

  Future<List<Horse>> getAllHorses() async
  {
    final response = await http.get(HORSES_URL);

    if (response.statusCode == 200)
    {
      return _parseHorses(response.body);
    }
    else
      {
      throw Exception('Failed to get horses!');
    }
  }

  Future<Horse> getHorse(Horse horse) async
  {
    final url = '$HORSES_URL${horse.id}/';
    final response = await http.post(url);

    if (response.statusCode == 200)
    {
      return Horse.fromJson(jsonDecode(response.body));
    }
    else
    {
      throw Exception('Failed to get the horse!');
    }
  }

  Future<void> postHorse(Horse horse) async
  {
    final headers = <String, String>{'Content-Type': 'application/json; charset=UTF-8',};

    http.post(HORSES_URL, headers: headers, body: jsonEncode(horse.toJson()));
  }

  Future<void> putHorse(Horse horse) async
  {
    final url = '$HORSES_URL${horse.id}/';
    final headers = <String, String>{'Content-Type': 'application/json; charset=UTF-8',};

    http.put(url, headers: headers, body: jsonEncode(horse.toJson()));
  }

  Future<void> deleteHorse(int id) async
  {
    final url = '$HORSES_URL$id/';
    http.delete(url);
  }

  Future<void> syncData(List<Horse> horses) async
  {
    final url = '${HORSES_URL}delete_all/';
    final headers = <String, String>
    {
      'Content-Type': 'application/json; charset=UTF-8',
    };
    await http.get(url);
    log(jsonEncode(horses));
    await http.post(HORSES_URL, headers: headers, body: jsonEncode(horses));
  }
}
