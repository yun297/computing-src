// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables

import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

void main() => runApp(MyApp());

@override
class MyApp extends StatelessWidget {
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: Scaffold(
        body: Center(
          child: Container(
              alignment: Alignment.topLeft,
              padding: EdgeInsets.all(24.0),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        child: Text("Location"),
                        margin: EdgeInsets.only(bottom: 8.0),
                      ),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Container(
                            margin: EdgeInsets.only(right: 4),
                            child: Icon(Icons.location_on),
                          ),
                          Text("City Hall, Singapore"),
                          Container(
                            margin: EdgeInsets.only(left: 4.0),
                            child: Icon(Icons.arrow_drop_down),
                          ),
                        ],
                      ),
                    ],
                  ),
                  Wrap(
                    children: [Icon(Icons.notifications)],
                  )
                ],
              )),
        ),
      ),
    );
  }
}