// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
//import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries


export default class Controller {
  firebase: any

  constructor() {
    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    const firebaseConfig = {
      apiKey: "AIzaSyAbW1UTb7jJ3_iDoETP-ghzvwV5Vad5q5Y",
      authDomain: "cwoc-50222.firebaseapp.com",
      projectId: "cwoc-50222",
      storageBucket: "cwoc-50222.appspot.com",
      messagingSenderId: "975454985849",
      appId: "1:975454985849:web:8032a2e79cd75b223ebea8",
      measurementId: "G-Y0VVSZP3T8"
    }

    // Initialize Firebase
    this.firebase = initializeApp(firebaseConfig)
    //this.analytics = getAnalytics(app);
  }
}
