import { ColorModeContext, useMode } from "./theme";
import { CssBaseline, ThemeProvider } from '@mui/material';
import { Routes, Route } from "react-router-dom";
import Patients from "./components/Patients";
import Doctors from "./components/Doctors";
import Topbar from './scenes/global/Topbar';
import Dashboard from "./scenes/dashboard";
import Sidebar  from "./scenes/global/Sidebar"
/* import { Patients } from "./scenes/patients"
import { Doctors } from "./scenes" */

function App() {
  const [theme, colorMode] = useMode();

  return (
    <ColorModeContext.Provider value= {colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline/>
        <div className='app'>
          <Sidebar />
          <main className='content'>
            <Topbar/>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/patients" element={<Patients />} />
              <Route path="/doctors" element={<Doctors />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  )
}

export default App;
