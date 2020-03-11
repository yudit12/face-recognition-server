const handleGetProfile=(req,res,db)=>{ // in this syntax -> /profile/: we can enter in the browser any anything 
    
    //  // with file  as database
    // const {id} = req.params;
    // let found =false
    // database.users.forEach(user=>{
    //     if( user.id ===id){
    //         found=true
    //         return res.json(user)
    //     }
    // })
    // if(!found){
    //     res.status(400).json('not found')
    // }

    const {id} = req.params;
    db.select('*').from('users')
    .where({
        id: id
    })
    .then(user=>{
        // console.log(user[0])
        if (user.length)// res if  found  a user in the db 
        {
            res.json(user[0])
        }
        else{
            res.status(400).json('user not found')
        }
       
    })
    .catch(err=>res.status(400).json('error geting user'))
   
   

}

module.exports={
    handleGetProfile: handleGetProfile
};