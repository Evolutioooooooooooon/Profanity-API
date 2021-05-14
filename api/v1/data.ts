import { Request, Response } from 'express'

const data = (req: Request, res: Response) => {
    return (
        res.send('Welcome to Profanity API! \n2021 Team Sirius - Chul0721. © All Rights Reserved.')
    )
}

export default data