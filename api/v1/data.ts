import { Request, Response } from 'express'
import getData from '../../utils/getData'
const words = require('../../assets/data.json')

const data = (req: Request, res: Response) => {
    if(!req.query.message) return res.send('Error: You need to give a message parameter value. \n2021 Team Sirius - Chul0721. © All Rights Reserved.')
    let apiData = words.data
    function x() {
        for(let i = 0; i < apiData.length; i++) {
            let result = getData(i, apiData, req.query.message)
            if(!result) return false
        }
        return true
    }
    if(x()) {
        return res.send('clean')
    } else {
        return res.send('cuss')
    }
}

export default data