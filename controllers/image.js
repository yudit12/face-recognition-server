
const  Clarifai = require('clarifai') ;


// API key for face-recognition
const app = new Clarifai.App({
    apiKey: '8da3226684994f8faf45b80b68ec4f93'
   });

   const hanleApiCall=(req,res)=>{
    app.models
        .predict(Clarifai.FACE_DETECT_MODEL,req.body.input)
        .then(data=>{
            res.json(data);
        })
        .catch(err=>res.status(400).json('unable to work with API'))
  

   }


const handleImage=(req,res,db)=>{
    // // using file  as database
    // const {id} = req.body;
    // let found =false
    // database.users.forEach(user=>{
    //     if( user.id ===id){
    //         found=true;
    //         user.entries++;
    //         return res.json(user.entries);
    //     }
    // })
    // if(!found){
    //     res.status(400).json('not found');
    // }

    const {id} = req.body;
    db('users').where('id', '=', id)
    .increment('entries',1)// column to increment , the amount to incre
    .returning('entries')
    .then(entries=>{
        // console.log(entries)
        res.json(entries[0])
    })
    .catch(err=>res.status(400).json('unable geting entries '))
}

module.exports={
    handleImage: handleImage,
    hanleApiCall: hanleApiCall
};