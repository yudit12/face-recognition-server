const handleRegister=(req,res,db,bcrypt)=>{
    
    // with file  as database
    // const {email, name,password }= req.body
    // database.users.push({
    //     id:'125',
    //     name: name,
    //     email:email,
    //     // password: password,
    //     entries: 0,
    //     joined :new Date()

    // })
    // res.json(database.users[database.users.length-1])
   
    const {email, name,password }= req.body
    //  convert passwords to hash - for safety 
    const hash =bcrypt.hashSync(password);// store pasword
        /* 
        transaction- when we doing multiple action for example when  insert to multiple table check that the action succeed in all tables
        only if succeeded in all tables return and save result in the db 
        first update loging table then users table*/
        db.transaction(trx=>{
          trx.insert({
              hash: hash,
              email: email
          })
          .into ('login')
          .returning('email')
           .then (loginEmail=>{
                return trx('users')
                    .returning('*')// return the new user 
                    .insert({
                        email: loginEmail[0],
                        name: name,
                        joined: new Date()
                    })//. then (console.log)// then (console.log)  insert the val to  the db 
                    .then (user=>{
                        res.json(user[0])
                    })
           })
           .then(trx.commit)
           .catch(trx.rollback)
        })    
            //  .catch(err=> res.status(400).json(err))// this sending db info - creates security usesnot good!!
        .catch(err=> res.status(400).json("unable to register "))

}

module.exports={
    handleRegister: handleRegister
};