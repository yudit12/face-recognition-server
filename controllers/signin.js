const handleSignin=(req,res,db,bcrypt)=>{
    //  // using file  as database
    // if(req.body.email===database.users[0].email &&req.body.password===database.users[0].password)
    // {
    //     // res.json("success")
    //     res.json(database.users[0])
        
    // }
    // else{
    //     res.status(400).json('error logging in ')
    // }
    db.select('hash','email').from('login')
    .where('email','=',req.body.email)
    .then(data=>{
        const isValid=bcrypt.compareSync(req.body.password,data[0].hash);
        if(isValid)
        {
            return db.select('*').from('users')
            .where('email','=', req.body.email)
            .then(user=>{
                res.json(user[0])
            })
            .catch(err=> res.status(400).json("unable to get user "))
        }
        else
        {
            res.status(400).json(" wrong credentials ")
        }
        
    })
    .catch(err=> res.status(400).json(" wrong credentials "))


}

module.exports={
    handleSignin: handleSignin
};