import { Request, Response } from 'express'

const postRequest = (req: Request, res: Response) => {
    return (
        res.send('Error: This API does not support any POST requests. Please use GET request. \n2021 Team Sirius - Chul0721. © All Rights Reserved.')
    )
}

export default postRequest