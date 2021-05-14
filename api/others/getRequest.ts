import { Request, Response } from 'express'

const getRequest = (req: Request, res: Response) => {
    return (
        res.send('Error: This API does not support any GET requests. Please use POST request. \n2021 Team Sirius - Chul0721. © All Rights Reserved.')
    )
}

export default getRequest