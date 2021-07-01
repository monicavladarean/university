import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../horse_notifier.dart';
import 'add_horse.dart';
import 'horse_detail.dart';

class HorseList extends StatefulWidget
{
  HorseList({Key key, this.name}) : super(key: key);

  final String name;

  @override
  _HorseListState createState() => _HorseListState();
}

class _HorseListState extends State<HorseList>
{
  @override
  Widget build(BuildContext context) {
    HorseNotifier horseNotifier = Provider.of<HorseNotifier>(context);

    return Scaffold(
      backgroundColor: Colors.amberAccent,
      appBar: AppBar(
        title: Text('My Horses'),
        backgroundColor: Colors.green,
        elevation: 0.0,
      ),
      body: Container(
        margin: EdgeInsets.fromLTRB(17, 0, 17, 0),
        child: ListView.builder(
            itemCount: horseNotifier.horses.length,
            itemBuilder: (BuildContext context, int index) {
              return Container(
                margin: EdgeInsets.fromLTRB(0, 17, 0, 0),
                child: GestureDetector(
                  child: Card(
                    child: Row(
                      children: [
                        Container(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                horseNotifier.horses[index].name,
                                overflow: TextOverflow.ellipsis,
                                style: TextStyle(
                                  fontSize: 30.0,
                                  color: Colors.brown,
                                ),
                              ),
                            ],
                          ),
                        )
                      ],
                    ),
                  ),
                  onTap: () {
                    Navigator.push(context,MaterialPageRoute(builder: (context) => HorseDetail(horse: horseNotifier.horses[index])),);
                  },
                ),
              );
            }),
      ),
      floatingActionButton: FloatingActionButton(
        child: Icon(Icons.add),
        onPressed: () {
          _navigateToAddHorse(context);
        },
      ),
    );
  }

  _navigateToAddHorse(BuildContext context) async
  {
    await Navigator.push(context, MaterialPageRoute(builder: (context) => AddHorseForm()),);
  }
}
