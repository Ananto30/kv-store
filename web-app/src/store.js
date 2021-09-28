import { writable } from "svelte/store";

export const page = writable("services");
export const service = writable("");

export const host = writable("localhost");
export const port = writable(6379);
export const db = writable(0);

export const needConnect = writable(false);