import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import * as z from 'zod';
import { apiClient } from '../../lib/api-client';
import {CONFIG} from '../../core/config';

const loginSchema = z.object({
    username: z.string().min(1, "username is required"),
    password: z.string().min(6, "Password must atleast be 6 characters"),
});

type loginFormValues = z.infer<typeof loginSchema>;

export default function LoginPage() {{
    const navigate = useNavigate();
    const {register, handleSubmit, formState: {errors, isSubmitting}} = useForm<loginFormValues>({
        resolver: zodResolver(loginSchema),
    });

    const onSubmit = async (data: loginFormValues) => {
        try {
            const formData = new FormData();
            formData.append('username', data.username);
            formData.append('password', data.password);

            const response = await apiClient.post('/login', formData);

            localStorage.setItem('token', response.data.access_token);

            navigate('/dashboard');
        } catch (error) {
            alert("Invalid credentials. Please check your FastAPI console");
        }
    };

    return (
        <div className='flex min-h-screen items-center justify-center'>
            <div>
                <h2>{CONFIG.COMPANY_NAME} Login</h2>

                <form onSubmit={handleSubmit(onSubmit)}>
                    <div>
                        <label>Username</label>
                        <input
                        {...register('username')}
                        />
                        {errors.username && <p>{errors.username.message}</p>}
                    </div>.
                    <div>
                        <label>Password</label>
                        <input
                        type='password'
                        {...register('password')}
                        />
                        {errors.password && <p>{errors.password.message}</p>}
                    </div>

                    <button
                    disabled={isSubmitting}
                    >
                        {isSubmitting ? 'Authenticating' : 'Sign In'}
                    </button>
                </form>
            </div>
        </div>
    );
}}