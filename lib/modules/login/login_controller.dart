import 'package:flutter/material.dart';
import 'package:google_sign_in/google_sign_in.dart';
import 'package:payflow/shared/auth/auth_controller.dart';
import 'package:payflow/shared/models/user_model.dart';

class LoginController {
  final authController = AuthController();
  GoogleSignIn _googleSignIn = GoogleSignIn(
    scopes: [
      'email',
    ],
  );
  
  Future<void> googleSignIn(BuildContext context) async {
    
    try {
      final response = await _googleSignIn.signIn();
      final user = UserModel(
        name: response!.displayName!,
        photoURL: response.photoUrl,
      );
      authController.setUser(context, user);
      print(response);
    } catch (error) {
      authController.setUser(context, null);
      print(error);
    }
  }
  Future<void> googleLogOut(BuildContext context) async {
    try {
      await _googleSignIn.signOut();
      authController.logOut();
      Navigator.pushReplacementNamed(context, "/login");
    } catch (e) {
      print(e);
    }
  }
}