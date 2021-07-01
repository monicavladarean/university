class Horse
{
  int id;
  String name;
  int age;
  String breed;
  String food;
  String disease;

  Horse({this.id, this.name, this.age, this.breed, this.food, this.disease});

  factory Horse.fromJson(Map<String, dynamic> json)
  {
    return Horse(
      id: json['id'],
      name: json['name'],
      age: json['age'],
      breed: json['breed'],
      food: json['food'],
      disease: json['disease'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name':name,
      'age':age,
      'breed':breed,
      'food':food,
      'disease':disease
    };
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name':name,
      'age':age,
      'breed':breed,
      'food':food,
      'disease':disease
    };
  }

  @override
  String toString()
  {
    return 'Horse{id: $id, name: $name, age: $age, breed: $breed, food: $food, disease: $disease}';
  }
}
