import * as express from "express";
import * as dotenv from "dotenv";
import * as cors from "cors";
import router from "../routes";

dotenv.config({ path: "../.env" });
const app = express();
const port = process.env.PORT || 8080;
const corsOptions = {
  origin: "*",
};
const urlencodedOptions = {
  extended: true,
};

app.use(router);
app.use(cors(corsOptions));
app.use(express.json());
app.use(express.urlencoded(urlencodedOptions));
app.set("trust proxy", true);

app.listen(port, () => {
  console.log(
    "\x1b[36m%s\x1b[34m%s\x1b[0m",
    "[Server]",
    `  Server on  : ${port}`
  );
});
