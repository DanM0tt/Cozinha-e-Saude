import React, { useState } from 'react';
import './Login.css';
import IlustracaoX1 from '/home/vinicius/nutricin-frontend/src/assets/imagem1.2.png'; 
import IlustracaoX2 from '/home/vinicius/nutricin-frontend/src/assets/imagem2.png'; 
// Importe as imagens (X1 e X2) e ícones (Google e Facebook)
// No React, você geralmente faria o import da imagem e usaria a variável no src
// Ex: import LogoX2 from './caminho/para/logo-x2.png';

// Importe os ícones do Google e Facebook (usando fontes ou SVG simplificados para este exemplo)
// Para um projeto real, você usaria uma biblioteca de ícones como react-icons.

// URLs dos ícones (apenas para exemplo, você deve usar seus próprios SVGs ou fontes de ícones)
const googleIconUrl = 'https://upload.wikimedia.org/wikipedia/commons/5/53/Google_%22G%22_Logo.svg';
const facebookIconUrl = 'https://upload.wikimedia.org/wikipedia/commons/b/b5/2021_Facebook_icon.svg';

const Login = () => {
    // Hooks de estado para controlar os valores dos inputs (Componentes Controlados)
    const [usuario, setUsuario] = useState('');
    const [senha, setSenha] = useState('');

    const handleLogin = (e) => {
        e.preventDefault();
        // Lógica de autenticação aqui (ex: enviar para o backend)
        console.log('Tentativa de Login:', { usuario, senha });
    };

    const handleSocialLogin = (provider) => {
        // Lógica para login social (ex: Firebase Auth, Auth0, etc.)
        console.log(`Login com ${provider}`);
    };

    return (
        <div className="login-page">
            <div className="image-section">
                {/* O componente X1 é a imagem ilustrativa maior */}
                {/* Substitua './caminho/para/x1.png' pela sua imagem real */}
                 <img src={IlustracaoX1} alt="Ilustração" className="x1-image" />
            </div>

            <div className="login-container">
                {/* O componente X2 é o logo menor acima do formulário */}
                {/* Substitua './caminho/para/x2.png' pela sua imagem real */}
                <img src={IlustracaoX2} alt="Ilustração" className="x2-image" />

                <div className="login-form-box">
                    <h2 className="login-title">LOGIN</h2>
                    
                    <form onSubmit={handleLogin} className="login-form">
                        <label htmlFor="usuario">Usuário</label>
                        <input
                            type="text"
                            id="usuario"
                            value={usuario}
                            onChange={(e) => setUsuario(e.target.value)}
                            placeholder="Seu nome de usuário ou e-mail"
                            required
                            className="login-input"
                        />

                        <label htmlFor="senha">Senha</label>
                        <input
                            type="password"
                            id="senha"
                            value={senha}
                            onChange={(e) => setSenha(e.target.value)}
                            placeholder="Sua senha"
                            required
                            className="login-input"
                        />

                        <div className="social-login-section">
                            <span className="social-text">Entrar com:</span>
                            <div className="social-buttons">
                                <button
                                    type="button"
                                    className="social-button google"
                                    onClick={() => handleSocialLogin('Google')}
                                >
                                    <img src={googleIconUrl} alt="Google" className="social-icon" />
                                </button>
                                <button
                                    type="button"
                                    className="social-button facebook"
                                    onClick={() => handleSocialLogin('Facebook')}
                                >
                                    <img src={facebookIconUrl} alt="Facebook" className="social-icon" />
                                </button>
                            </div>
                        </div>

                        <button type="submit" className="button primary-button">
                            ENTRAR
                        </button>
                        
                        <a href="#" className="forgot-password">Recuperar senha?</a>
                    </form>
                </div>

                <button 
                    type="button" 
                    className="button secondary-button"
                    onClick={() => console.log('Ir para Cadastro')} // Substitua pela lógica de navegação
                >
                    CADASTRAR
                </button>
            </div>
        </div>
    );
};

export default Login;