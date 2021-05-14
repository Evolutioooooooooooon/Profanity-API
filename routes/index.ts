import { Router } from 'express'
import { main, data, notFound, postRequest } from '../api'

const router = Router()

router.get('/api/v1/', main)
router.get('/api/v1/data', data)
router.get('*', notFound)
router.post('*', postRequest)

export default router