import { Request, Response } from "express";

const main = (req: Request, res: Response) => {
  return res.send(
    "<h1>Welcome to Profanity API!</h1><br><h5>2021 Team Sirius - Chul0721. © All Rights Reserved.</h5>"
  );
};

export default main;
