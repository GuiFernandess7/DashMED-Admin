import axios from 'axios';

const delay = () => new Promise(res => setTimeout(() => res(), 800))

/* CRUD OPERATIONS  */

const APIAccess = axios.create({
  baseURL: 'http://localhost:8080',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const createEntity = async (endpoint, data) => {
  await delay()
  const response = await APIAccess.post(endpoint, data);
  return response.data;
};

export const readEntity = async (endpoint) => {
  const response = await APIAccess.get(endpoint);
  return response.data;
};

export const updateEntity = async (endpoint, data) => {
  await delay()
  const response = await APIAccess.put(endpoint, data);
  return response.data;
};

export const deleteEntity = async (endpoint) => {
  await delay()
  const response = await APIAccess.delete(endpoint);
  return response.data;
};
