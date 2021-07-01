import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../horse.dart';
import '../horse_notifier.dart';

class UpdateHorseForm extends StatefulWidget
{
  final Horse horse;

  const UpdateHorseForm({Key key, @required this.horse}) : super(key: key);

  @override
  UpdateHorseFormState createState() {
    return UpdateHorseFormState(horse);
  }
}

class UpdateHorseFormState extends State<UpdateHorseForm>
{
  final _formKey = GlobalKey<FormState>();
  final Horse horse;

  final _nameInputController = TextEditingController();
  final _ageInputController = TextEditingController();
  final _breedInputController = TextEditingController();
  final _foodInputController = TextEditingController();
  final _diseaseInputController = TextEditingController();

  UpdateHorseFormState(this.horse);

  @override
  Widget build(BuildContext context) {
    HorseNotifier horseNotifier = Provider.of<HorseNotifier>(context);

    _nameInputController.text = horse.name;
    _ageInputController.text = horse.age.toString();
    _breedInputController.text = horse.breed;
    _foodInputController.text = horse.food;
    _diseaseInputController.text = horse.disease;

    return Scaffold(
      backgroundColor: Colors.amberAccent,
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: Text('Update the horse'),
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
                    if (int.tryParse(value) == null ||
                        int.tryParse(value) < 0) {
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
                        horseNotifier.update(
                            horse.id,
                            _nameInputController.text,
                            int.parse(_ageInputController.text),
                            _breedInputController.text,
                            _foodInputController.text,
                            _diseaseInputController.text
                            );
                      });

                      Navigator.of(context).pop();
                    }
                  },
                  child: Text('Update horse!'),
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
