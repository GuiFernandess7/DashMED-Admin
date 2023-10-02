import * as apiService from './apiService';

export const doctorsEndpoint = '/doctors';

export const getDoctors = () => {
    apiService.readEntity(doctorsEndpoint);
}

/* export const createDoctor = (data) => apiService.createEntity(doctorsEndpoint, data);

export const updateDoctor = (data) => apiService.updateEntity(doctorsEndpoint, data);

export const deleteDoctor = () => apiService.deleteEntity(doctorsEndpoint);
 */