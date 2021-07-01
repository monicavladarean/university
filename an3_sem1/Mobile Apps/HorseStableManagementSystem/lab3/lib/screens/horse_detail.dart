import 'package:flutter/material.dart';
import 'package:lab3/screens/update_horse.dart';
import 'package:provider/provider.dart';

import '../horse.dart';
import '../horse_notifier.dart';

class HorseDetail extends StatelessWidget {
  final Horse horse;

  HorseDetail({Key key, @required this.horse}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    HorseNotifier horseNotifier = Provider.of<HorseNotifier>(context);
    Horse currentHorse = horseNotifier.horse(horse.id);

    return Scaffold(
      body: Container(
        child: Column(
          children: <Widget>[
            _horseMainDetails(currentHorse),
            Container(
              margin: EdgeInsets.only(top: 30),
              child: Card(
                child: Container(
                  padding: EdgeInsets.all(15),
                  child: Column(
                    children: [
                      Text('Horse name'),
                      SizedBox(height: 5),
                      Text(currentHorse.name),
                      SizedBox(height: 20),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Builder(
                            builder: (ctx) => Container(
                              width: 150,
                              child: ElevatedButton(
                                onPressed: () {
                                  _showDeleteDialog(context, horseNotifier);
                                },
                                child: Text('Delete!'),
                                style: ElevatedButton.styleFrom(
                                  primary: Colors.green,
                                ),
                              ),
                            ),
                          ),
                          Builder(
                            builder: (ctx) => Container(
                              width: 150,
                              child: ElevatedButton(
                                onPressed: () {
                                  _navigateToUpdateHorse(context, currentHorse);
                                },
                                child: Text('Update!'),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                    crossAxisAlignment: CrossAxisAlignment.start,
                  ),
                ),
              ),
            ),
          ],
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
        ),
        padding: EdgeInsets.all(32.0),
      ),
    );
  }

  _navigateToUpdateHorse(BuildContext context, Horse horse) async
  {
    await Navigator.push(context,MaterialPageRoute(builder: (context) => UpdateHorseForm(horse: horse)),);
  }

  Future<void> _showDeleteDialog(
      BuildContext context, HorseNotifier horseNotifier) async {
    return showDialog<void>(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(
            'Are you sure you want to delete this horse?',
            textAlign: TextAlign.center,
          ),
          actions: <Widget>[
            TextButton(
              child: Text('Yes!'),
              onPressed: () {
                horseNotifier.remove(horse.id);
                Navigator.of(context).popUntil((route) => route.isFirst);
              },
            ),
            TextButton(
              child: Text('No.'),
              onPressed: () {
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }

  Widget _horseMainDetails(Horse currentHorse) {
    return Container(
      child: Row(
        children: [
          Column(
            children: [
              Text(currentHorse.name),
            ],
            crossAxisAlignment: CrossAxisAlignment.start,
          ),
        ],
      ),
    );
  }
}
