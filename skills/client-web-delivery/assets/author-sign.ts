// Authorship fingerprint ms-<FINGERPRINT> (Miguel Sanchez): marks the footer so a copied page carries it.
import { SIG } from "../scripts/sig";
export const sign = (html: string) => html.replace(/<footer(?![^>]*data-ms)/, `<footer data-ms="${SIG}"`);
