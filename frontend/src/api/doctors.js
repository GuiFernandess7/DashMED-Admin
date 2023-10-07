import * as apiService from './service';

export const doctorsEndpoint = '/doctors';

export const getDoctors = () => {
    return apiService.readEntity(doctorsEndpoint);
}

/* export const createDoctor = (data) => apiService.createEntity(doctorsEndpoint, data);

export const updateDoctor = (data) => apiService.updateEntity(doctorsEndpoint, data);

export const deleteDoctor = () => apiService.deleteEntity(doctorsEndpoint);
 */