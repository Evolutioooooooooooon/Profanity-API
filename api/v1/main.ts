import { Request, Response } from 'express'

const main = (req: Request, res: Response) => {
    return (
        res.send('Welcome to Profanity API! \n2021 Team Sirius - Chul0721. © All Rights Reserved.')
    )
}

export default main