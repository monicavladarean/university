import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../horse_notifier.dart';

class AddHorseForm extends StatefulWidget
{
  @override
  AddHorseFormState createState() {
    return AddHorseFormState();
  }
}

class AddHorseFormState extends State<AddHorseForm>
{
  final _formKey = GlobalKey<FormState>();

  final _nameInputController = TextEditingController();
  final _ageInputController = TextEditingController();
  final _breedInputController = TextEditingController();
  final _foodInputController = TextEditingController();
  final _diseaseInputController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    HorseNotifier horseNotifier = Provider.of<HorseNotifier>(context);

    return Scaffold(
      backgroundColor: Colors.amberAccent,
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Text('Add a new horse'),
        backgroundColor: Colors.amberAccent,
        elevation: 0.0,
        centerTitle: false,
      ),
      body: Container(
        color: Colors.amberAccent,
        margin: EdgeInsets.fromLTRB(17, 0, 17, 0),
        child: SingleChildScrollView(
          child: Form(
            key: _formKey,
            child: Column(
              children: <Widget>[
                TextFormField(
                  controller: _nameInputController,
                  decoration: InputDecoration(labelText: 'Name:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'name';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _ageInputController,
                  decoration: InputDecoration(labelText: 'Age:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'age';
                    }
                    if (int.tryParse(value) == null) {
                      return 'Please enter a positive integer';
                    }

                    if (int.tryParse(value) < 0) {
                      return 'Please enter a positive integer';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _breedInputController,
                  decoration: InputDecoration(labelText: 'Breed:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'breed';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _foodInputController,
                  decoration: InputDecoration(labelText: 'Food:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'food';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  controller: _diseaseInputController,
                  decoration: InputDecoration(labelText: 'Disease:'),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'disease';
                    }

                    return null;
                  },
                ),
                ElevatedButton(
                  onPressed: () {
                    if (_formKey.currentState.validate()) {
                      setState(() {
                        horseNotifier.add(
                            _nameInputController.text,
                            int.parse(_ageInputController.text),
                            _breedInputController.text,
                            _foodInputController.text,
                            _diseaseInputController.text);
                      });

                      Navigator.of(context).popUntil((route) => route.isFirst);
                    }
                  },
                  child: Text('Add horse!'),
                  style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                  ),
                ),
              ],
              crossAxisAlignment: CrossAxisAlignment.stretch,
              mainAxisAlignment: MainAxisAlignment.start,
            ),
          ),
          padding: EdgeInsets.fromLTRB(14, 0, 14, 0),
        ),
      ),
    );
  }
}
