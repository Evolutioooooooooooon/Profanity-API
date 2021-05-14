import express from 'express'
import { main, data, notFound, getRequest } from '../api'

const router = express.Router()

router.post('/v1/', main)
router.post('/v1/data', data)
router.post('*', notFound)
router.get('*', getRequest)

export default router