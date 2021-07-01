import 'package:flutter/material.dart';
import 'package:lab3/screens/horse_list.dart';
import 'package:provider/provider.dart';
import 'horse_notifier.dart';

void main() => runApp(
  ChangeNotifierProvider(
    create: (context) => HorseNotifier(),
    child: MyHorses(),
  ),
);

class MyHorses extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MyHorses',
      theme: ThemeData(
        primarySwatch: Colors.green,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: HorseList(name: 'MyHorses'),
    );
  }
}