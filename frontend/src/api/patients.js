import * as apiService from './service';

export const patientsEndpoint = '/patients';

export const getPatients = async () => {
    return apiService.readEntity(patientsEndpoint);
}

/* export const createPatient = (data) => apiService.createEntity(patientsEndpoint, data);

export const updatePatient = (data) => apiService.updateEntity(patientsEndpoint, data);

export const deletePatient = () => apiService.deleteEntity(patientsEndpoint);
 */