import { Request, Response } from "express";

const notFound = (req: Request, res: Response) => {
  return res.send(
    "404 Error: This is a false route. Please use /api/v1/ route. \n2021 Team Sirius - Chul0721. © All Rights Reserved."
  );
};

export default notFound;
