/*
REST API defines set of function which developers can perform requst and recive response
via HTTP protocol such as GET, POST, PUT , DELETE
- it an approach to communications, an agreed upon set 
GET- to recive a resource --> for example: /profile  we will get profile
PUT- to change a state or update a resource -->/profile  we will update profile
POST- creates a resource -->/profile  we will update profile
DELETE - to remove it 


/--> res= this working
/signin -->POST = success/fail
/register--> POST= user (new user object)
/profile/:userID--> GET =user
/image--> PUT --> user (updae user object)

*/



const express =require('express');
const bodyParser= require('body-parser');// parse json from frontent to backend 
const bcrypt= require('bcrypt-nodejs');// change password to hash 
const cors= require('cors');// Allows server and client to run on the same browser (on different ports)
const knex= require('knex'); // for conecting to the DB
const register= require('./controllers/register.js');
const signin= require('./controllers/signin.js');
const profile= require('./controllers/profile.js');
const image= require('./controllers/image.js');

const db= knex({
    client: 'pg',
    connection: {
      host : '127.0.0.1', //localhost
      user : 'postgres',
      password : '1234',
      database : 'postgres'
    }
});



db.select('*').from('users').then(data=>{
    console.log(data)
})

const app= express();
app.use(bodyParser.json());
app.use(cors());
// const  database={
//     users:[
//         {
//             id:'111',
//             name: 'g',
//             email:'g',
//             password: '123',
//             entries: 0,
//             joined :new Date()


//         },
//         {
//             id:'123',
//             name: 'john',
//             email:'jjj@gmail.com',
//             password: 'xxxxxxxx',
//             entries: 0,
//             joined :new Date()


//         },
//         {
//             id:'456',
//             name: 'dddd',
//             email:'dddd@gmail.com',
//             password: 'ggggggggg',
//             entries: 0,
//             joined :new Date()


//         }
//     ]
// }

app.get('/',(req,res)=>{
    // res.send('this is working')
    res.send(database.users)
})

// siginin 
app.post('/signin',(req,res)=>{signin.handleSignin(req, res,db,bcrypt)})
// create new user
app.post('/register',(req,res)=>{register.handleRegister(req, res,db,bcrypt)})


// for profile page for each  user
app.get('/profile/:id',(req,res)=>{profile.handleGetProfile(req, res,db)} )

// update the user, increase is img entries count
app.put('/image',(req,res)=>{image.handleImage(req, res,db)})

app.post('/imageUrl',(req,res)=>{image.hanleApiCall(req, res)})

app.listen(process.env.PORT ||3000,()=>{
    console.log(`app is running on port ${process.env.PORT}`)
});

